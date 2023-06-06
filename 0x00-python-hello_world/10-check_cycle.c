#include "lists.h"

/**
 * check_cycle - check if there is a cycle or not
 * @list: head of linked list
 *
 * Return: 1 if cycled, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list ? list->next : NULL;

	while (fast && fast->next)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}
