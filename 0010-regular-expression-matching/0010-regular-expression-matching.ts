function isMatch(s: string, p: string): boolean {
    const m: number = s.length;
    const n: number = p.length;
    const f: boolean[][] = Array.from({ length: m + 1 }, () => Array(n + 1).fill(false));

    f[0][0] = true;

    for (let i = 0; i <= m; ++i) {
        for (let j = 1; j <= n; ++j) {
            if (p[j - 1] === '*') {
                f[i][j] = f[i][j - 2];
                if (i > 0 && (p[j - 2] === '.' || p[j - 2] === s[i - 1])) {
                    f[i][j] = f[i][j] || f[i - 1][j];
                }
            } else if (i > 0 && (p[j - 1] === '.' || p[j - 1] === s[i - 1])) {
                f[i][j] = f[i - 1][j - 1];
            }
        }
    }

    return f[m][n];
}
