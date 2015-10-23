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

%token <str> EVERYDAY
%token <str> PREPOSITION
%token <str> MESSAGE
%token <str> WORD
%token <str> TIME DATE

%type<str> wish message preposition time day

%%

wish:
        message preposition time preposition day         {
                                                                printf("{");
                                                                printf("\"message\":\"%s\",", $1);
                                                                printf("\"date\":\"%s\",", $5);
                                                                printf("\"time\":\"%s\"", $3);
                                                                printf("}");
                                                            }
        | message preposition day preposition time         {
                                                                printf("{");
                                                                printf("\"message\":\"%s\",", $1);
                                                                printf("\"date\":\"%s\",", $3);
                                                                printf("\"time\":\"%s\"", $5);
                                                                printf("}");
                                                            }

        | message preposition time day {
                                                printf("{");
                                                printf("\"message\":\"%s\",", $1);
                                                printf("\"date\":\"%s\",", $4);
                                                printf("\"time\":\"%s\"", $3);
                                                printf("}");
                                            }
        | message preposition day time {
                                                printf("{");
                                                printf("\"message\":\"%s\",", $1);
                                                printf("\"date\":\"%s\",", $3);
                                                printf("\"time\":\"%s\"", $4);
                                                printf("}");
                                            }

        | message day preposition time      {
                                                printf("{");
                                                printf("\"message\":\"%s\",", $1);
                                                printf("\"date\":\"%s\",", $2);
                                                printf("\"time\":\"%s\"", $4);
                                                printf("}");
                                            }
        | message time preposition day      {
                                                printf("{");
                                                printf("\"message\":\"%s\",", $1);
                                                printf("\"date\":\"%s\",", $4);
                                                printf("\"time\":\"%s\"", $2);
                                                printf("}");
                                            }
        | message preposition time          {
                                                printf("{");
                                                printf("\"message\":\"%s\",", $1);
                                                printf("\"time\":\"%s\"", $3);
                                                printf("}");
                                            }
        | message preposition day          {
                                                printf("{");
                                                printf("\"message\":\"%s\",", $1);
                                                printf("\"date\":\"%s\"", $3);
                                                printf("}");
                                            }
    | message day time          {
                                            printf("{");
                                            printf("\"message\":\"%s\",", $1);
                                            printf("\"time\":\"%s\",", $3);
                                            printf("\"date\":\"%s\"", $2);
                                            printf("}");
                                        }
        | message day preposition time          {
                                                printf("{");
                                                printf("\"message\":\"%s\",", $1);
                                                printf("\"time\":\"%s\",", $4);
                                                printf("\"date\":\"%s\"", $2);
                                                printf("}");
                                            }
    | message day          {
                                            printf("{");
                                            printf("\"message\":\"%s\",", $1);
                                            printf("\"date\":\"%s\"", $2);
                                            printf("}");
                                        }
        | message                             {
                                                printf("{");
                                                printf("\"message\":\"%s\"", $1);
                                                printf("}");
                                            }


message:
        MESSAGE                             {$$ = $1;}

preposition:
        PREPOSITION                         {$$ = $1;}

time:
        TIME                                {$$ = $1;}

day:
        WORD                                {$$ = $1;}
        | EVERYDAY                          {$$ = $1;}
        | DATE                              {$$ = $1;}

%%

void yyerror(char *s) {
    fprintf(stderr, "%s\n", s);
}

int main(void) {
    yyparse();
    return 0;
}
