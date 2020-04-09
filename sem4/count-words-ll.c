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
char* mystrdup (char *s);

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
	while(p != NULL){
		printf("%4d %s\n", p->count, p->word);
		p = p->next;
	}
}

//add: adds a node with a new word at or below p
struct listnode *add(struct listnode *p, char *w){
	int cond,cond2; 

	if (p == NULL){ //new word
		p = talloc();
		p -> word = strdup(w);
		p -> count = 1;
		p -> next = NULL;
	} else if (p->next!= NULL){
	 	if ((cond= strcmp(w,p->next->word)) < 0){ //gretaer than, 
			if (strcmp(w,p->word) > 0)
				{
				struct listnode* nuevo;
				nuevo = talloc();
				nuevo-> word = strdup(w);
				nuevo-> count = 1;
				nuevo-> next = p->next;

				return nuevo;
				} else
					p->count++;
		}
		else if(cond > 0)
			p = add(p->next, w);
		else if(cond == 0)
			p->next->count++;	
	}else{
		if ((cond2 =strcmp(w,p->word)) == 0)
			p->count++;		
		else if(cond2 > 0){
			struct listnode* nuevo;
			nuevo = talloc();
			nuevo-> word = strdup(w);
			nuevo-> count = 1;
			nuevo-> next = NULL;
			p->next = nuevo;
		}
			
		else{
			struct listnode* nuevo;
			nuevo = talloc();
			nuevo-> word = strdup(w);
			nuevo-> count = 1;
			nuevo->next = p;

			return nuevo;
		}
	}
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

char *mystrdup(char *s){
	char *p;

	p = (char *) malloc(strlen(s)+1); //+1 for '\0'
	if (p!= NULL)
		strcpy(p,s);
	return p;
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