#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h> //maloc and releated routines

#define MAXWORD	100
#define getch() getchar()
#define ungetch(c) ungetc(c, stdin)

struct listnode *add(struct listnode *, char *);
void listprint(struct listnode *);
int getword(char *, int);
struct listnode *talloc(void);

void swap (struct listnode *, struct listnode *);

struct listnode
{
	char *word;
	int count;
	struct listnode *next;
};



int main()
{
	struct listnode *root;
	char word[MAXWORD];

	root = NULL;
	while(getword(word,MAXWORD) != EOF)
		if(isalpha(word[0]))
			root = add(root, word);
	listprint(root);
	return 0;
}

//imprime la lista enlazada de palabras
void listprint(struct listnode *p){
	if(p != NULL){
		listprint(p->next);
		printf("%4d %s\n", p->count, p->word);
	}
}

//add: adds a node with a new word at or below p
struct listnode *add(struct listnode *p, char*w){
	int cond;

	if (p == NULL){ //new word
		p = talloc();
		p -> word = strdup(w);
		p -> count = 1;
		p -> next = NULL;
	} else if ((cond = strcmp(w,p->next->word)) == 0)
		p->count++; //repeated word;
	else if (cond > 0){ //gretaer than, into left subtree
		swap(p,p->next);
		p->next = add(p->next, w);
	}
	else				//less than, into right subtree
		return p;
}

void swap (struct listnode *p, struct listnode *next){
	struct listnode* temp = NULL;
	temp = p;
	p = next;
	next = temp;
}







//talloc: makes a listnode
struct listnode *talloc(void){
	return (struct listnode *) malloc(sizeof(struct listnode));
}


//getword: get next word or character from input
int getword(char *word, int lim)
{
	int c;
	char *w = word;

	while(isspace(c = getch()))
		;
	if(c != EOF)
		*w++ = c;
	if(!isalpha(c)) {
		*w = '\0';
		return c;
	}
	for(; --lim>0; w++)
		if(!isalnum(*w = getch())){
			ungetch(*w);
			break;
		}
	*w = '\0';
	return word[0];
}