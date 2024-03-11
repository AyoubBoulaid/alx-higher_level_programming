#include "lists.h"
/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *S = list;
	listint_t *F = list;

	if (!list)
		return (0);

	while (S && F && F->next)
	{
		S = S->next;
		F = F->next->next;
		if (S == F)
			return (1);
	}
	return (0);
}
