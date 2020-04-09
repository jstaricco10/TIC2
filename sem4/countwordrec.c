#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#define getch() getchar()
#define ungetch(c) ungetc(c, stdin)
#define MAXWORD 100
struct listnode {
    char *word;
    int count;
    struct listnode *next;
};
int getword(char *, int);
struct listnode *addnode(struct listnode *, char *);
void listprint(struct listnode *);
int
main()
{
    struct listnode *root;
    char word[MAXWORD];
    root = NULL;
    while (getword(word, MAXWORD) != EOF)
        if (isalpha(word[0]))
            root = addnode(root, word);
    listprint(root);
    return 0;
}
struct listnode *lnalloc(void);
char *mystrdup(char *);
struct listnode *
addnode(struct listnode *p, char *w)
{
    int cond, cond2;
    struct listnode *temp;
    if (p == NULL)
    {
        p = lnalloc();
        p->word = strdup(w);
        p->count = 1;
        p->next = NULL;
    }
    else if (p->next != NULL) 
    {
        if ((cond = strcmp(w, p->next->word) < 0))
            if (strcmp(w, p->word) > 0)
            {
                struct listnode *n;
                n = lnalloc();
                n->word = strdup(w);
                n->count = 1;
                n->next = p->next;
                p->next = n;
                return n;
            }
            else
                p->count++;
        else if (cond > 0)
            return addnode(p->next, w);
        else if (cond == 0)
            p->next->count++;
    }
    else
    {
        if ((cond2 = strcmp(w, p->word)) == 0)
            p->count++;
        else if (cond2 > 0)
        {
             struct listnode *n;
             n = lnalloc();
             n->word = strdup(w);
             n->count = 1;
             n->next = NULL;
             p->next = n;
        }
        else
        {
            struct listnode *n;
            n = lnalloc();
            n->word = strdup(w);
            n->count = 1;
            n->next = p;
            return n;
        }
    }
    return p;
}
void
listprint(struct listnode *p)
{
    while (p != NULL)
    {   
        printf("%4d %s\n", p->count, p->word);
        p = p->next;
    }
}
struct listnode *
lnalloc(void)
{
    return (struct listnode *) malloc(sizeof(struct listnode));
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