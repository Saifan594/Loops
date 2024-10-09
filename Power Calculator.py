print ( "\033c" )

base = int ( input ( "enter the base : " ) )
power = int ( input ( "enter the power : " ) )

answer = 1

for i in range ( power ) :
    answer = answer * base

print ( f"\n{ base } to the power of { power } is equal to { answer }\n" )