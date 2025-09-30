function fourSumCount(nums1, nums2, nums3, nums4) {
    const cnt = new Map();
    for (const a of nums1) {
        for (const b of nums2) {
            const x = a + b;
            cnt.set(x, (cnt.get(x) || 0) + 1);
        }
    }
    let ans = 0;
    for (const c of nums3) {
        for (const d of nums4) {
            const x = c + d;
            ans += cnt.get(-x) || 0;
        }
    }
    return ans;
}
