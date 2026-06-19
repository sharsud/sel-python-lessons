#exception handling

# try:
#     #risky code
# except:
#     #code to handle the exceltion/error
#
# # Extended version of try except
# try:
#     #code section
# except Exception1:
#     #code to handle exception1
# except Exception2:
#     #code to handle exception2
# else:
#     #code ran with no exception
# finally:
#     #this code is always executed

#ticketing system
#Raising execp
# try:
#     num_ticket=int(input("Enter the number of ticket: "))
#     print("The number of ticket is",num_ticket)
# except ValueError:
#     print("The value entered is not a number")

# #driving license
# def check_age(age):
#     if age < 18:
#         raise ValueError("you are not allowed because age is less than 18")
#     print("you can apply for driving license")
#
# try:
#     check_age(18)
# except ValueError as e:
#     print("error ::",e)

# #custom error
# def book_tickets(num):
#     if num >5:
#         raise Exception("You cannot book more than 5 tickets")
#     print(f"You have {num} tickets booked")
#
# try:
#     book_tickets(int(input()))
# except Exception as e:
#     print(f"error: {e}")

# #else block
# try:
#     num=int(input("Enter the number of tickets: "))
#     if num<=0:
#         raise Exception("Invalid Number")
# except Exception as e:
#     print(e)
# else:
#     print("Proceeding to payment....")
#
#finally block
# try:
#     file=open("logs.txt","w")
#     file.write("Booked 5 tickets...")
# except FileNotFoundError:
#     print("No such file or directory")
# finally:
#     try:
#         file.close()
#         print("File closed")
#     except:
#         pass

#multiple Exceptions

# try:
#     num=int(input("Enter a number: "))
#     ticket_cost=100
#     total=ticket_cost/num
# except (ValueError, ZeroDivisionError) as e:
#     print(f"Oops! error occured :: {e}")
#

#Re-raising exceptions
# try:
#     num=int(input("Enter a number: "))
#     ticket_cost=100
#     total=ticket_cost/num
# except (ValueError, ZeroDivisionError) as e:
#     print(f"Oops! error occured :: {e}")
#     raise

# #supressing exceptions
# from contextlib import suppress
# with suppress(FileNotFoundError):
#     open("abc.txt")
#
# custom Exception class
class AgeTooSmallError(Exception):
    pass
def apply(age):
    if age < 18:
        raise AgeTooSmallError("YOu must be above the age of 18 to apply a DL")
    print("You can apply a DL")

try:
    apply(17)
except AgeTooSmallError as e:
    print(e)