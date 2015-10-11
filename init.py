from app import config
from app.db.Datastore import Datastore

#
# Setup Datastore
#
datastore = Datastore()
datastore.setup()

#
# Setup Application Config
#
initialConfig = {
}

for k, v in initialConfig.iteritems():
    if datastore.getConfig(k) == None:
        datastore.addConfig(k, v)
