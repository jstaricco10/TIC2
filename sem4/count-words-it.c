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
char *strdup(char *);
struct listnode *
addnode(struct listnode *root, char *w)
{
    int cond;
    struct listnode *temp = root;
    if (root == NULL)
    {
        root = lnalloc();
        root->word = strdup(w);
        root->count = 1;
        root->next = NULL;
        return root;
    }
    else
    {
        if ((cond = strcmp(w, root->word)) <= 0)
            if (cond == 0)
                root->count++;
            else
            {
                struct listnode *n;
                n = lnalloc();
                n->word = strdup(w);
                n->count = 1;
                n->next = root;
                root = n;
                return root;
            }
        else
        {
            while (temp->next != NULL)
            {
                if ((cond = strcmp(w, temp->next->word) == 0))
                {
                    temp->next->count++;
                    return root;
                }
                else if (cond < 0)
                {
                    struct listnode *n;
                    n = lnalloc();
                    n->word = strdup(w);
                    n->count = 1;
                    n->next = temp->next;
                    temp->next = n;
                    return root;
                }
                else
                    temp = temp->next;
            }
            if ((cond = strcmp(w, temp->word)) == 0)
            {
                temp->count++;
                return root;
            }
            else
            {
                struct listnode *n;
                n = lnalloc();
                n->word = strdup(w);
                n->count = 1;
                n->next = NULL;
                temp->next = n;
                return root;
            }
        }
    }
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
strdup(char *s)
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
