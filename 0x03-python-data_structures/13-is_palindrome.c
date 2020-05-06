#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head
 * Return: 1 if the node is a palindrome or 0 if not.
 */
int is_palindrome(listint_t **head)
{
	listint_t *aux1 = *head, *aux2 = *head;
	int i = 0, j, k;

	if (!*head)
		return (1);

	for (i = 0; aux1->next; i++, aux1 = aux1->next)
		;

	if (aux1->n != (*head)->n)
		return (0);
	if (i == 1)
		return (1);

	k = i - 2;

	while (i < (i / 2))
	{
		aux2 = aux2->next;
		aux1 = aux2;
		for (j = 0; j < k; j++)
			aux1 = aux1->next;
		if (aux2->n != aux1->n)
			return (0);
		i++;
		k = i - 2;
	}
	return (1);
}
