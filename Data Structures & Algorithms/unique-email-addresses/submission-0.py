class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_list = set()
        for email in emails:
            local = ""
            domain = ""
            #if it sees . ignore
            #if it sees + stop adding to local
            #if it sees @ start domain
            char = 0
            while email[char] != "@":
                if email[char] == ".":
                    char += 1
                    continue
                elif email[char] == "+":
                    while email[char] != "@":
                        char += 1
                    break
                else:
                    local += email[char]
                char += 1
            
            while char < len(email):
                domain += email[char]
                char += 1

            curr_email = local + domain
            if curr_email not in email_list:
                email_list.add(curr_email)

        return len(email_list)