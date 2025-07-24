function twoSum(arr: number[], target: number): number[] {
    const map: { [key: number]: number } = {};
    const ans: number[] = [];

    for (let i = 0; i < arr.length; i++) {
        const first = arr[i];
        const second = target - first;

        if (second in map) {
            ans.push(map[second]);
            ans.push(i);
            break;
        }

        map[first] = i;
    }

    return ans;
}
