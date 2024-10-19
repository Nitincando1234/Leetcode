class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        choices = set(("A", "C", "G", "T"))
        bank = set(bank)
        q = deque([(startGene, 0)])
        visit = {startGene}
        while q:
            gene, steps = q.popleft()
            if gene == endGene: return steps
            for i, s in enumerate(gene):
                for c in choices:
                    if s != c:
                        newGene = gene[: i] + c + gene[i + 1:]
                        if newGene in bank and newGene not in visit:
                            visit.add(newGene)
                            q.append((newGene, steps + 1))
        return - 1