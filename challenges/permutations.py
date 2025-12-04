def permute(nums):
    output = []

    def perms(prefix, remaining):
        if remaining == []:
            output.append(list(prefix))
            return

        for index in range(len(remaining)):
            prefix.append(remaining[index])
            new_remaining = remaining[0:index] + remaining[index + 1:]
            perms(prefix, new_remaining)
            prefix.pop()

    perms([], nums)
    return output
