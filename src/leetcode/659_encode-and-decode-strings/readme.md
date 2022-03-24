# Problem 659 Encode and Decode Strings

<https://leetcode.com/problems/encode-and-decode-strings/>

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings. Please implement encode and decode

**Example 1:**

    Input: [“lint”,“code”,“love”,“you”]
    Output: [“lint”,“code”,“love”,“you”]
    Explanation: One possible encode method is: “lint:;code:;love:;you”

**Example 2:**

    Input: [“we”, “say”, “:”, “yes”]
    Output: [“we”, “say”, “:”, “yes”]
    Explanation: One possible encode method is: “we:;say:;:::;yes”

**Solution:**

Basically, one of the easy solution is to define a delimiter which could be any special character like # or / to separate words in encode method. However, this special character might appear in the word in real world. We can get around it by appending an escaped character or size of the word. Here, we append the size of the word when encoding

    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        res = ''
        for s in strs:
            encoded = str(len(s)) + '/' + s
            res += encoded
        return res
    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        res, i = [], 0
        while i < len(str):
            # For example, 12/abc
            e = i
            while e < len(str) and str[e] != '/':
                e += 1
            size = int(str[i:e])
            word = str[e + 1, e + 1 + size]
            i = e + 1 + size
            res.append(word)
        return res

Space complexity: O(n)
Time complexity: O(n)
