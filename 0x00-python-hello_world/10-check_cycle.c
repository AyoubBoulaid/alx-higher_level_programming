#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to get checked
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *F, *S;

	if (list == NULL || list->next == NULL)
		return (0);

	F = list->next;
	S = list->next->next;

	while (S && F && F->next)
	{
		if (S == F)
			return (1);

		S = S->next;
		F = F->next->next;
	}

	return (0);
}
