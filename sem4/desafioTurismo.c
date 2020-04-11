#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#define getch() getchar()
#define ungetch(c) ungetc(c, stdin)
#define MAXWORD 100


struct lineasnode{
    int linea;
    struct lineasnode *proxAparcion;
};
struct listnode {
    char *word;
    struct lineasnode *lines;
    struct listnode *next;
};
int getword(char *, int);
struct listnode *addlistnode(struct listnode *, char *, int line);
struct lineasnode *addline(struct lineasnode *, int l);
void listprint(struct listnode *);
void linesprint(struct lineasnode *);
int
main()
{
    struct listnode *root;
    char word[MAXWORD];
    root = NULL;

    // char *linea = fgets()
    // while (){

    // }


    // while (getword(word, MAXWORD) != EOF){
        
    //     if (isalpha(word[0]))
    //         root = addlistnode(root, word,1);
    // }
    // listprint(root);
    return 0;
}
struct listnode *lnalloc(void);
struct linenode *linelistalloc(void);
char *mystrdup(char *);
struct listnode *
addlistnode(struct listnode *p, char *w, int line)
{
    int cond;
    if (p == NULL)
    {
        p = lnalloc();
        p->word = strdup(w);
        p->lines = addline(p->lines, line); 
        p->next = NULL;
    } else if ((cond = strcmp(w, p->word)) < 0){
        struct listnode *n;
        n = lnalloc();
        n->word = strdup(w);
        n->lines = addline(n->lines, line); 
        n->next = p;
        return n;
    } else if (cond == 0)
        p->lines = addline(p->lines, line); 
    else{
        p->next = addlistnode(p->next, w, line);
    }
    return p;
}

struct lineasnode *addline(struct lineasnode *ln, int l){
    int cond; 
    if (ln == NULL)
    {
        ln = linelistalloc();
        ln -> linea = l;
        ln -> proxAparcion = NULL;
    } else if (l == ln->linea){
        return ln;
    } else {
        ln->proxAparcion = addline(ln->proxAparcion, l);
    }
    return ln;
}

void
linesprint(struct lineasnode *ln){
    while(ln != NULL)
    {
        printf(" %d ",ln->linea);
        ln = ln -> proxAparcion;
    }
}

void
listprint(struct listnode *p)
{
    while (p != NULL)
    {   
        printf("%s", p->word);
        linesprint(p->lines);
        printf("\n");
        p = p->next;
    }
}

struct listnode *
lnalloc(void)
{
    return (struct listnode *) malloc(sizeof(struct listnode));
}

struct linenode *
linelistalloc(void)
{
    return (struct lineasnode *) malloc(sizeof(struct lineasnode));
}

char *
mystrdup(char *s)
{
    char *p;
    p = (char *) malloc(strlen(s) + 1);
    if (p != NULL)
        strcpy(p, s);
    return p;
}
int
getword(char *word, int lim)
{
    int c;
    char *w = word;
    while (isspace(c = getch()))
        ;
    if (c != EOF)
        *w++ = c;
    if (!isalpha(c)) {
        *w = '\0';
        return c;
    }
    for ( ; --lim > 0; w++ )
        if (!isalnum(*w = getch())) {
            ungetch(*w);
            break;
        }
    *w = '\0';
    return word[0];
}


