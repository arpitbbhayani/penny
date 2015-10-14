%{
    #include "remind.h"
    #include <stdio.h>
    int yylex(void);
    void yyerror(char *);
%}


%union
{
        char *str;
}

%token <str> PREPOSITION
%token <str> MESSAGE
%token <str> WORD
%token <str> TIME

%type<str> wish message preposition time

%%

wish:
        message preposition time            {
                                                printf("MESSAGE:%s\n", $1);
                                                printf("TIME:%s\n", $3);
                                            }

message:
        MESSAGE                             {$$ = $1;}

preposition:
        PREPOSITION                         {$$ = $1;}

time:
        TIME                                {$$ = $1;}

%%

void yyerror(char *s) {
    fprintf(stderr, "%s\n", s);
}

int main(void) {
    yyparse();
    return 0;
}
