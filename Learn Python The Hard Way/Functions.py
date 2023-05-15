def LetsCreate(*args): # this is just varargs
    print(type(args)) #<class 'tuple'>
    print(args[0]+":"+args[1]) #Hello:Phoenix

LetsCreate("Hello","Phoenix")#Hello:Phoenix
# LetsCreate(1,2,3) # error operator '+' cannot concatenate str and int