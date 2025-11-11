from typing import List, Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        """Funde duas listas ligadas ordenadas e retorna a lista ligada resultante."""
        result = ListNode(0)
        current = result  # Nó inicial vazio para facilitar a construção da lista resultante
        while l1 and l2:  # Percorre ambas as listas até que uma delas seja esgotada
            if l1.val <= l2.val:  # Compara os valores dos nós atuais
                current.next = l1  # Adiciona o nó de l1 à lista resultante
                l1 = l1.next  # Avança para o próximo nó em l1
            else:
                current.next = l2  # Adiciona o nó de l2 à lista resultante
                l2 = l2.next  # Avança para o próximo nó em l2
            current = current.next
        if l1:  # Se ainda houver nós restantes em l1, adiciona-os à lista resultante
            current.next = l1
        if l2:  # Se ainda houver nós restantes em l2, adiciona-os à lista resultante
            current.next = l2
        return result.next  # Retorna o próximo nó, ignorando o nó inicial vazio

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        result = []
        interval = 1  # Intervalo inicial para mesclagem
        # Continua até que o intervalo seja maior ou igual ao número de listas
        while interval < len(lists):
            # Mescla as listas em pares com o intervalo atual
            for i in range(0, len(lists) - interval, interval * 2):
                # Mescla listas em pares
                lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2  # Dobra o intervalo para a próxima rodada de mesclagem
        return lists[0]
