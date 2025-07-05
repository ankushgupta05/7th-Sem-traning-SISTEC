📘 C Programming Revision Notes – Arrays, Characters, and Memory Behavior


---

✅ 1. int arr[5] = {1, 2, 3};

int arr[5] = {1, 2, 3};
printf("%d", arr[3]);

First 3 elements: 1, 2, 3

Remaining 2 elements (arr[3], arr[4]) auto-initialized to 0

✅ Output: 0



---

✅ 2. char arr[5] = {'a', 'b', 'c'};

char arr[5] = {'a', 'b', 'c'};
printf("%c", arr[3]);

First 3 elements: 'a', 'b', 'c'

arr[3] and arr[4] auto-initialized to \0 (null char)

✅ %c prints nothing (null is non-printable)

✅ %d prints: 0



---

✅ 3. Capacity of char arr[5]

🔹 When using as a character array (raw data):

You can store 5 characters: 'a', 'b', 'c', 'd', 'e'

No need for \0 unless manually added


🔹 When using as a string (for printing via %s):

You need space for null terminator \0

So max usable characters = 4


Examples:

char arr[5] = "abcd";   // ✅ OK (4 chars + '\0')
char arr[5] = "abcde";  // ❌ Not safe (no space for '\0')

🔹 Detailed Example:

char arr[5] = {'A', 'B', 'C', 'D', 'E'};
for (int i = 0; i < 5; i++)
    printf("%c ", arr[i]);
// ✅ Output: A B C D E

char str[5] = "ABCD";
printf("%s", str);
// ✅ Output: ABCD

char str[5] = "ABCDE";
printf("%s", str);
// ❌ May cause undefined behavior (no null terminator)


---

✅ 4. Summary of String Initialization:

char str[] = "abc";     // Size = 4 (includes \0)
char str[5] = "abc";    // ✅ Valid, extra space
char str[3] = "abc";    // ❌ Invalid (no space for \0)


---

✅ 5. Important Notes

%c prints single character

%s prints characters until it hits \0

%d prints ASCII or integer value


Let me know if you want the notes exported as a PDF or markdown file!



I've expanded the section on char and string usage with detailed explanations and examples, especially focusing on how much data can be stored when the array size is 5.

Let me know if you'd like a visual diagram, export to PDF/Markdown, or examples with pointers and char *str.

