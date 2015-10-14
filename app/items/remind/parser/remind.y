%{
    #include "remind.h"
    #include <stdio.h>
    int yylex(void);
    void yyerror(char *);
%}

%token ON AT COLON

%union
{
        int num;
        char *str;
}

%token <str> MESSAGE
%token <str> WORD
%token <num> NUMBER

%type<num> time
%type<str> wish message

%%

wish:
        message AT time     {printf("MESSAGE\t%s\nTIME\t%d", $1, $3);}

message:
        MESSAGE             {$$ = $1;}

time:
        NUMBER              {$$ = $1;}


%%
void yyerror(char *s) {
    fprintf(stderr, "%s\n", s);
}

int main(void) {
    yyparse();
    return 0;
}
