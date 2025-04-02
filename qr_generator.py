import qrcode
import os
from PIL import Image # Pillow library is needed by qrcode for image operations

def generate_qr_code(data, filename="qrcode.png", error_correction='M', box_size=10, border=4):
    """
    Generates a QR code image from the given data.

    Args:
        data (str): The text or URL to encode.
        filename (str): The desired name for the output image file (e.g., "my_qr.png").
                        Defaults to "qrcode.png".
        error_correction (str): The error correction level ('L', 'M', 'Q', 'H').
                                Defaults to 'M' (Medium).
        box_size (int): The size of each box (pixel) in the QR code grid.
                        Defaults to 10.
        border (int): The thickness of the border (in boxes).
                      Defaults to 4 (standard).

    Returns:
        bool: True if QR code was generated and saved successfully, False otherwise.
    """
    if not data:
        print("Error: No data provided to encode.")
        return False

    # Ensure filename has a .png extension if not provided
    if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
         # Default to png if extension is missing or invalid for basic saving
        base, _ = os.path.splitext(filename)
        filename = base + ".png"
        print(f"Warning: Output format adjusted to PNG. Saving as: {filename}")


    # Map error correction level string to qrcode constants
    error_correction_map = {
        'L': qrcode.constants.ERROR_CORRECT_L, # About 7% or less errors can be corrected.
        'M': qrcode.constants.ERROR_CORRECT_M, # About 15% or less errors can be corrected.
        'Q': qrcode.constants.ERROR_CORRECT_Q, # About 25% or less errors can be corrected.
        'H': qrcode.constants.ERROR_CORRECT_H  # About 30% or less errors can be corrected.
    }
    ec_level = error_correction_map.get(error_correction.upper(), qrcode.constants.ERROR_CORRECT_M)
    if ec_level != error_correction_map.get(error_correction.upper()):
        print(f"Warning: Invalid error correction level '{error_correction}'. Using default 'M'.")


    try:
        # Create QR code instance
        qr = qrcode.QRCode(
            version=None, # Let the library choose the smallest appropriate version
            error_correction=ec_level,
            box_size=box_size,
            border=border,
        )

        # Add data to the QR code
        qr.add_data(data)
        qr.make(fit=True) # Finalize the QR code structure

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image
        img.save(filename)
        print(f"Successfully generated QR code and saved as '{filename}'")
        return True

    except FileNotFoundError:
        print(f"Error: Could not save file. The path or directory for '{filename}' might not exist.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

# --- Main Execution ---
if __name__ == "__main__":
    print("--- QR Code Generator ---")

    # Get input data from user
    data_to_encode = input("Enter the text or URL to encode: ")

    # Get desired filename from user (optional)
    output_filename = input("Enter the desired output filename (e.g., my_qr.png) [Press Enter for 'qrcode.png']: ")
    if not output_filename:
        output_filename = "qrcode.png" # Default filename

    # Generate the QR code
    generate_qr_code(data_to_encode, output_filename)

    print("-------------------------")
