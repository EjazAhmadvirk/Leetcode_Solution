function firstUniqChar(s: string): number {
    const m = new Map<string, number>();
    const Q: number[] = [];

    for (let i = 0; i < s.length; i++) {
        const char = s[i];

        if (!m.has(char)) {
            Q.push(i);
        }

        m.set(char, (m.get(char) || 0) + 1);

        while (Q.length > 0 && m.get(s[Q[0]])! > 1) {
            Q.shift();
        }
    }

    return Q.length === 0 ? -1 : Q[0];
}
