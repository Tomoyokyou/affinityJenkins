# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to 
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.

def highest_affinity(site_list, user_list, time_list):
    # Returned string pair should be ordered by dictionary order
    # I.e., if the highest affinity pair is "foo" and "bar"
    # return ("bar", "foo").

    # Traverse the site list & user list and then build a hashmap which key is site and value is user
    site_visited = {}

    for i in range(len(site_list)):
        if site_list[i] in site_visited:
            site_visited[site_list[i]].add(user_list[i])
        else:
            site_visited[site_list[i]] = set([user_list[i]])

    # Find the largest intersection of two different sites as the return site pair

    high_aff_pair = ()
    high_num = 0

    for site1 in site_visited:
        for site2 in site_visited:
            if site1 != site2:
                tmp_num = len(site_visited[site1].intersection(site_visited[site2]))
                if tmp_num > high_num:
                    # Sort the returned tuple lexicographically
                    if site1>site2:
                        high_aff_pair = (site2, site1)
                    else:
                        high_aff_pair = (site1, site2)
                    high_num = tmp_num

    return high_aff_pair


def highest_affinity2(site_list, user_list, time_list):
    # Returned string pair should be ordered by dictionary order
    # I.e., if the highest affinity pair is "foo" and "bar"
    # return ("bar", "foo").

    # Traverse the site list & user list and then build a hashmap which key is site and value is user
    site_visited = {}

    for i in range(len(site_list)):
        if site_list[i] in site_visited:
            site_visited[site_list[i]].add(user_list[i])
        else:
            site_visited[site_list[i]] = set([user_list[i]])

    # Find the largest intersection of two different sites as the return site pair

    high_aff_pair = ()
    high_num = 0

    for site1 in site_visited:
        for site2 in site_visited:
            if site1 != site2:
                tmp_num = len(site_visited[site1].intersection(site_visited[site2]))
                if tmp_num > high_num:
                    # Sort the returned tuple lexicographically
                    if site1 > site2:
                        high_aff_pair = (site2, site1)
                    else:
                        high_aff_pair = (site1, site2)
                    high_num = tmp_num

    return high_aff_pair
