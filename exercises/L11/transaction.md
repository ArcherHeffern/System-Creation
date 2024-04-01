# SQL Transaction for Transfering Funds
## Basic Version
```sql
BEGIN TRANSACTION;

-- Debit the source account
UPDATE Accounts
SET Balance = Balance - @Amount
WHERE AccountID = @SourceAccountID;

-- Credit the destination account
UPDATE Accounts
SET Balance = Balance + @Amount
WHERE AccountID = @DestinationAccountID;

-- Commit the transaction if both updates succeed
COMMIT TRANSACTION;
```

## Advanced Version
Creates a function, and checks the destination has enough funds

```sql
CREATE PROCEDURE TransferFunds
    @SourceAccountID INT,
    @DestinationAccountID INT,
    @Amount DECIMAL(10, 2)
AS
BEGIN
    DECLARE @SourceBalance DECIMAL(10, 2);
    
    -- Check if the source account has enough balance
    SELECT @SourceBalance = Balance
    FROM Accounts
    WHERE AccountID = @SourceAccountID;

    IF @SourceBalance >= @Amount
    BEGIN
        BEGIN TRANSACTION;

        -- Debit the source account
        UPDATE Accounts
        SET Balance = Balance - @Amount
        WHERE AccountID = @SourceAccountID;

        -- Credit the destination account
        UPDATE Accounts
        SET Balance = Balance + @Amount
        WHERE AccountID = @DestinationAccountID;

        -- Commit the transaction if both updates succeed
        COMMIT TRANSACTION;

        PRINT 'Funds transferred successfully.';
    END
    ELSE
    BEGIN
        PRINT 'Insufficient funds in the source account. Transfer canceled.';
    END
END;
```
