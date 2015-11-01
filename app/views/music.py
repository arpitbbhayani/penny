import random

from flask import Blueprint

from flask import request, render_template
from flask import url_for, make_response, jsonify
from flask_restful import reqparse

from flask import render_template

from app.service import musicService

mod = Blueprint('music', __name__, )

@mod.route('/', methods=["GET"])
def index():
    # Playlists
    playlists_meta = musicService.get_playlists_meta_info()
    return render_template('pages/music_widget.html', playlists=playlists_meta)


@mod.route('/playlist/<playlist_id>', methods=["GET"])
def get_playlist(playlist_id):
    error, playlist = musicService.get_playlist(playlist_id)
    return render_template('playlist.html', error=error, playlist=playlist)


@mod.route('/playlist/<playlist_id>/add', methods=["POST"])
def add_links_to_playlist(playlist_id):
    parser = reqparse.RequestParser()
    parser.add_argument('link', type=str, help='link cannot be empty', location='form')
    parser.add_argument('site', type=str, help='site cannot be empty', location='form')
    args = parser.parse_args()

    error, meta_info = musicService.add_links_to_playlist(playlist_id, args.get('link'), args.get('site'))

    return jsonify(resp=meta_info, error=error)


@mod.route('/playlist/<playlist_id>/random', methods=["GET"])
def get_random_from_playlist(playlist_id):
    error, link_info = musicService.get_random_link(playlist_id)
    return jsonify(resp=link_info, error=error)


@mod.route('/playlist/<playlist_id>/all', methods=["GET"])
def all_from_playlist_randomly(playlist_id):
    error, links = musicService.get_links_in_playlist(playlist_id)
    random.shuffle(links)
    return jsonify(resp=links, error=error)


@mod.route('/playlist/create', methods=["POST"])
def create_playlist():
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, help='name cannot be empty', location='form')
    args = parser.parse_args()

    error, playlistObj = musicService.create_playlist(args.get('name'))

    playlist_html = render_template('one-playlist.html', playlist=playlistObj) if playlistObj else None

    return jsonify(resp=playlistObj, html=playlist_html, error=error)


@mod.route('/playlist/delete', methods=["POST"])
def delete_playlist():
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=str, help='id cannot be empty', location='form')
    args = parser.parse_args()

    error, ret = musicService.delete_playlist(args.get('id'))

    return jsonify(resp=ret, error=error)
