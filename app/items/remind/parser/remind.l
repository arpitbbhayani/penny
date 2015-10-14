%{
    #include <string.h>
    #include <stdio.h>
    #include "y.tab.h"
%}

%%
\"[^"]*\"               {yylval.str = strdup(yytext); return MESSAGE;}
on                      return ON;
at                      return AT;
:                       return COLON;
[0-9]+                  {yylval.num = atoi(yytext); return NUMBER;}
[a-zA-Z][a-zA-Z0-9]*    {yylval.str = yytext; return WORD;}
[ \t\n]+                ;
.                       {printf("Invalid character\n");}
%%

int yywrap(void) {
    return 1;
}
