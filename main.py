def main():
    number = 0
    while True:
        try:
          number = int(input("Enter A number:"))
          if 1<= number < 100:
              break
          else:
              print("retry")
        except ValueError:
              print("Invalid")
    print(f"{number}")
   
    """
    ########################################
    Code Your Program here
    ########################################
    """

    ########################################
    # Do not delete the return statement
    ########################################
    return number


if __name__ == '__main__':
    main()
