import os

class LicenseGenerator:
    @classmethod
    def default(cls, product, company_name="Digital Down", output_folder="."):
        if product is None:
            raise ValueError("Product name must be provided")

        license_text = f"""#License for {product}

## License Grant

{product}, provided by {company_name}, is offered free of charge. You are granted a non-exclusive, non-transferable license to use the software under the following terms:

## Allowed Use

1. **Generated Products**: You are allowed to use {product} to generate content or products. You may sell, distribute, or otherwise commercially exploit the products or content created using {product}.

2. **Source Code**: You may access, view, and modify the source code of {product} for personal or internal use only.

## Restrictions

1. **Software Redistribution**: You may not redistribute, sublicense, or otherwise transfer copies of {product} or its source code to others without explicit permission.

2. **Commercial Use of Software**: You may not use {product} itself for commercial purposes. This includes, but is not limited to, providing the software as a service or using it in any commercial enterprise.

3. **Derivative Works**: You may not create derivative works based on {product} without explicit permission.

## Disclaimer

{product} is provided "as is," without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and non-infringement. In no event shall {company_name} be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software."""

        # Create the full path for the LICENSE.txt file
        license_path = os.path.join(output_folder, "LICENSE.txt")

        # Write the license text to the file
        with open(license_path, "w") as license_file:
            license_file.write(license_text)

        print(f"LICENSE.txt has been generated for {product} by {company_name} in {os.path.abspath(output_folder)}.")