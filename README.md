# USSD Service

A simple USSD (Unstructured Supplementary Service Data) service simulation in Python, allowing users to check their balance, transfer credits, and pay bills via a command-line interface (CLI).

## Features

- **Transfer Pulsa**: Transfer credit to another phone number.
- **Cek Saldo**: Check your current balance.
- **Bayar Tagihan**: Pay your bills using the available balance.

## How It Works

The USSD Service consists of a main menu that lets users interact with three main options: transferring pulsa, checking their balance, and paying bills. Users can enter commands via the command line to perform these actions, and the balance will be updated accordingly.

## Quick Start

To run this project, follow the steps below:

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/ussd-service.git
   ```

2. Navigate to the project directory:

   ```bash
   cd ussd-service
   ```

3. Run the Python script:

   ```bash
   python ussd_service.py
   ```

### Example Usage

Upon running the script, you'll be presented with a simple menu:

1. Transfer Pulsa
2. Cek Saldo
3. Bayar Tagihan
4. Keluar

#### Transfer Pulsa

- Enter the recipient's phone number and the amount to transfer.
- If the recipient is valid and your balance is sufficient, the transfer will be successful.

#### Cek Saldo

- Displays the current balance of the user.

#### Bayar Tagihan

- Enter the bill ID to pay, and if the balance is sufficient, the bill will be paid successfully.

## Code Structure

- `USSDService`: A class that simulates the USSD service.
  - `transfer_pulsa(phone_number, amount)`: Transfers pulsa (credit) to a specified phone number.
  - `cek_saldo()`: Displays the current balance of the user.
  - `bayar_tagihan(bill_id)`: Pays the specified bill.
  - `main_menu()`: Displays the interactive menu and handles user input.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request.

---

### Author

**Fausta Akbar Wijaya**

Feel free to reach out to me via [LinkedIn](https://www.linkedin.com/in/faustaakbar/) or [GitHub](https://github.com/FaustaAkbar) if you have any questions or suggestions!
