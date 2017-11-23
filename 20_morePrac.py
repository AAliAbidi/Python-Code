print("Let's practice everything.")
print("You\'d need to know \' but escape with \\that do \n new line and \t tabs ")
poem = """ 
     \t The lovely world
     with logic so firmly planted
     cannot discern \n the needs of love
     nor comprehend passion from intution
     and requirs an explanation
     \n\t\twhere there is none."""

print("----------------")
print (poem)
print("----------------")

five = 10-2+3-6
print("This shoul be five %s" %five)

def secret_formula(startd):
    jelly_beans = startd * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 1000
beans, jars, crate = secret_formula(start_point)

print("With starting point of %d" %start_point)
print("we'd have %d beans, %d jars and %d cates." %(beans,jars,crate))

start_point = start_point / 10

print("We can also do this way:")
print("we'd have %d beans, %d jars and %d cates." %(beans,jars,crate))


