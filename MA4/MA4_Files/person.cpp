#include <cstdlib> 

// Person class 

class Person{
	public:
		Person(int);
		int get();
		void set(int);
		int fib();
	private:
		int age;
	};
 
Person::Person(int n){
	age = n;
	}

int Person::fib(){
	if (get() <= 1)
		return (get());
	else {
		return Person(get()-1).fib() + Person(get()-2).fib();
}
}
 
int Person::get(){
	return age;
	}
 
void Person::set(int n){
	age = n;
	}


extern "C"{
	Person* Person_new(int n) {return new Person(n);}
	int Person_get(Person* person) {return person->get();}
	void Person_set(Person* person, int n) {person->set(n);}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}