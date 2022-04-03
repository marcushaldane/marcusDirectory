# HOMEWORK 6: Associate Law Fails
# Marcus Haldane

# Demonstrates how the Associative Law fails with floating point variables 
# being added together when being calculated on modern computers
.data
# floating point values to be used to demonstrate the limitations of computers in regards to the Associative Law
A:      .float 10000000000000000000000000000		# Holds A
B:	.float -10000000000000000000000000000		# Holds B
C:	.float 0.00000000000000000000000012345		# Holds C 

# string values to be used to produce a nice result in the "RUN I/O" console
Intro:		.asciiz 	"The Associative Law fails in the following example:\n"
TopLine:	.asciiz 	"Using:" 
Product1: 	.asciiz 	"a + (b + c) = " 
Product2: 	.asciiz 	"(a + b) + c = "
aM: 		.asciiz 	" a = "
bM: 		.asciiz 	", b = "
cM: 		.asciiz		", c = "
endline: 	.asciiz 	"\n"

.text
	# the following block of code is used to print out information before
	# calculations take place 
        li	$v0, 4          # Tell System to print a string
        la	$a0, Intro 	# Print Intro message
        syscall			# Tells System to print what is in $a0
        la 	$a0, TopLine	# Loads "Using:" into $a0
        syscall			# Tells System to print what is in $a0
        la	$a0, aM		# Loads " a = " into $a0
        syscall			# Tells System to print what is in $a0
	li	$v0, 2		# Tell System to print a floating point value
        lwc1	$f12, A		# Loads 10000000000000000000000000000 into $f12
        syscall			# Tells System to print what is in $f12
        li	$v0, 4          # Tell System to print a string
        la	$a0, bM		# Loads ", b = " into $a0
        syscall			# Tells System to print what is in $a0
        li	$v0, 2		# Tell System to print a floating point value
        lwc1	$f12, B		# Loads -10000000000000000000000000000 into $f12
        syscall			# Tells System to print what is in $f12
        li	$v0, 4          # Tell System to print a string
        la	$a0, cM		# Loads ", c = " into $a0
        syscall			# Tells System to print what is in $a0
        li	$v0, 2		# Tell System to print a floating point value
        lwc1	$f12, C		# Loads 0.00000000000000000000000012345 into $f12
        syscall			# Tells System to print what is in $f12
        li	$v0, 4          # Tell System to print a string
        la	$a0, endline	# Loads "\n" into $a0
        syscall			# Tells System to print what is in $a0
        syscall			# Tells System to print what is in $a0
        
        # the following block of code is used calculate and print the result of 
        # the products: A + (B + C) and (A + B) + C
        # precalculation of terms in parenthesis
        lwc1 	$f2, A		# Load A to a coprocessor register
        lwc1	$f3, B		# Load B to a coprocessor register
        lwc1	$f4, C		# Load C to a coprocessor register
	add.s	$f5, $f3, $f4	# $f5 = (b + c)
	add.s	$f6, $f2, $f3	# $f6 = (a + b)
	# printing of the results
	la	$a0, Product1	# Loads "a + (b + c) = " into $a0
	syscall			# Tells System to print what is in $a0
	li	$v0, 2		# Tell System to print a floating point value
        add.s	$f12, $f2, $f5	# $f12 = A + (B + C)
        syscall			# Tells System to print what is in $f12
        li	$v0, 4          # Tell System to print a string
        la	$a0, endline	# Loads "\n" into $a0
        syscall			# Tells System to print what is in $a0	
        la	$a0, Product2	# Loads "(a + b) + c = " into $a0
        syscall			# Tells System to print what is in $a0
        li	$v0, 2		# Tell System to print a floating point value
	add.s	$f12, $f4, $f6	# $f12 = (A + B) + C
        syscall			# Tells System to print what is in $f12
        
        # the following instructions terminate the program
        li,	$v0, 10		# Get termination code 
        syscall			# Terminate program
