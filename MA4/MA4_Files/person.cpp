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
		int fib_res(int);
	};
 
Person::Person(int n){
	age = n;
	}

int Person::fib(){
		return fib_res(self.age);
}

int Person::fib_res(int a){
	if (age <= 1)
		return (age);
	else 
		return fib_res(a-1) + fib_res(a-2);
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
	int Person_fib(Person* person) {return person->fib();}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}	
	