#include <linux/init.h>
#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/list.h>
#include <linux/types.h>
#include<linux/slab.h>


struct birthday{
 int day;
 int month;
 int year;
 struct list_head list;
};

static LIST_HEAD(birthday_list);

/* this function is called when the module is loaded*/
int simple_init(void)
{
struct birthday *person;
struct birthday *person2;
struct birthday *ptr;

person = kmalloc(sizeof(person),GFP_KERNEL);
person->day = 2;
person->month = 8;
person->year = 1995;
person2 = kmalloc(sizeof(person),GFP_KERNEL);
person2->day = 10;
person2->month = 8;
person2->year = 1995;
INIT_LIST_HEAD(&person->list);
list_add_tail(&person->list,&birthday_list);
list_add_tail(&person2->list,&birthday_list);


list_for_each_entry(ptr,&birthday_list,list){
 /*on each iteration ptr points to the next birthday struct*/
    printk("salam %d", ptr->day);
}

    printk(KERN_INFO "Loading Module\n");
 return 0;
}
/* this function is called when the module is removed*/
void simple_exit(void)
{
 printk(KERN_INFO "Removing Module\n");
}
/* Macros for registering module entry and exit points.*/
module_init(simple_init);
module_exit(simple_exit);
MODULE_LICENSE("GPL");
MODULE_DESCRIPTION("simple module");
MODULE_AUTHOR("SGG");