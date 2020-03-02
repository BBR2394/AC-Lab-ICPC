#ifndef BOOK_HH_
# define BOOK_HH_

#include <String>

class Book
{
public:
	Book();
	~Book();

private: 
	String _title;
	/* maybe a list of string for the author */
	String _author;

public:
	String getTitle();
};

#endif