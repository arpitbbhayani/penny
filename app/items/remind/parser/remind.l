%{
    #include <ctype.h>
    #include <string.h>
    #include <stdio.h>
    #include "y.tab.h"
    #include "remind.h"
%}

ws          [ \t]+
integer     [0-9]+

%%

\"[^"]*\"                                           {yylval.str = strdup(yytext); return MESSAGE;}
on|at|in                                            {yylval.str = strdup(yytext); return PREPOSITION;}
{integer}([:.]{integer})?{ws}?([aApP][mM])?         {yylval.str = strdup(yytext); return TIME;}
[a-zA-Z][a-zA-Z0-9]*                                {yylval.str = strdup(yytext); return WORD;}
[ \t\v\n\f]                                         ;
.                                                   {printf("Invalid character %c\n", *yytext);}
%%

void strlower(char *p) {
    for ( ; *p; ++p) {*p = tolower(*p);}
}

int yywrap(void) {
    return 1;
}
