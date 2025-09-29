function removeElement(nums: number[], val: number): number {
    let k = 0; // pointer for next valid position
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== val) {
            nums[k] = nums[i];
            k++;
        }
    }
    return k;
}
