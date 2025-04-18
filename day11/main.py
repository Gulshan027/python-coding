#funcition with outputs
# def my_function():
#     result=3*2
#     return result
# ans=my_function()
# print(ans)


# def format_name(f_name,l_name):
#     print(f_name.title())
#     print(l_name.title())
# format_name("angellaa","AGNGELGA")


# def format_name(f_name,l_name):
#     return f"{f_name.title()} {l_name.title()}"
     
# formateed_string= format_name("angellaa","AGNGELGA")
# print(formateed_string)



#more than one return


def format_name(f_name,l_name):
    if f_name=="" or l_name=="":
        return
    else:
        return f"{f_name} and {l_name}"
    
formated=format_name("gulshan","yadav")
print(formated)