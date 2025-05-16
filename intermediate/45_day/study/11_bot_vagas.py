# Loop para aplicar nas vagas automaticamente

for listing in all_listings:
    print("Opening Listing")
    listing.click()  # Abre a vaga
    time.sleep(2)
