#include <stdio.h>
#include <ctype.h>
#include <string.h>

//maloc and releated routines
#include <stdlib.h>

struct tnode	// the tree node
{
	char *word;				//pointer to the text
	int count;				//number of ocurrences
	struct tnode *left;		//left child (less)
	struct tnode *right;	//right child (more)
};


#define MAXWORD	100
#define getch() getchar()
#define ungetch(c) ungetc(c, stdin)
struct tnode *addtree(struct tnode *, char *);
void treeprint(struct tnode *);
int getword(char *, int);

//word frequency count
int main()
{
	struct tnode *root;
	char word[MAXWORD];

	root = NULL;
	while(getword(word,MAXWORD) != EOF)
		if(isalpha(word[0]))
			root = addtree(root, word);
	treeprint(root);
	return 0;
}



struct tnode *talloc(void);
//char *strdup(char *);

// addtree: add a node with w, at or below p
struct tnode *addtree(struct tnode *p, char*w)
{
	int cond;

	if(p == NULL){ // a new word has arrived
		p = talloc();
		p->word = strdup(w);
		p->count = 1;
		p->left = p->right = NULL;
	} else if ((cond = strcmp(w,p->word)) == 0)
		p->count++; //repeated word;
	else if (cond < 0) //les than, into left subtree
		p->left = addtree(p->left,w);
	else				//greater than, into right subtree
		p->right = addtree(p->right,w);
	return p;
};

//treeprint; in-order print of tree p
void treeprint(struct tnode *p){
	if (p != NULL)
	{
		treeprint(p-> left);
		printf("%4d %s\n", p->count, p->word);
		treeprint(p-> right);
	}
}

//talloc: makes a tnode
struct tnode *talloc(void){
	return (struct tnode *) malloc(sizeof(struct tnode));
}

//strdup: makes a duplicate of s. strdup marely copies the
// string given by irs argument into a safe place, obtained
// by a call on malloc;
// char *strdup(char *s){
// 	char *p;

// 	p = (char *) malloc(strlen(s)+1); //+1 for '\0'
// 	if (p!= NULL)
// 		strcpy(p,s);
// 	return (char*) place;
// }

	



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