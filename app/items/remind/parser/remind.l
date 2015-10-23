%{
    #include <ctype.h>
    #include <string.h>
    #include <stdio.h>
    #include "y.tab.h"
    #include "remind.h"
%}

ows         [ \t\r]*
integer     ([0-9]+)

%%

\"[^"]*\"                                               {yytext[strlen(yytext)-1] = 0; yytext++; yylval.str = strdup(yytext); return MESSAGE;}
everyday|every{ows}day                                  {yylval.str = strdup(yytext); return EVERYDAY;}
on|at|in                                                {yylval.str = strdup(yytext); return PREPOSITION;}
{integer}{ows}([:.]{ows}{integer})?{ows}([apAP][mM])?   {yylval.str = strdup(yytext); return TIME;}
{integer}[\-\.\:\/]{integer}([\-\.\:\/]{integer})?      {yylval.str = strdup(yytext); return DATE;}
[a-zA-Z][a-zA-Z0-9]*                                    {yylval.str = strdup(yytext); return WORD;}
[ \t\v\f\n]                                               ;
.                                                       {printf("Invalid character %c\n", *yytext);}
%%

void strlower(char *p) {
    for ( ; *p; ++p) {*p = tolower(*p);}
}

int yywrap(void) {
    return 1;
}
