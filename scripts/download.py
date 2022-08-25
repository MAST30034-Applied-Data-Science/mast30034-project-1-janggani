{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "e242f1c0",
   "metadata": {},
   "outputs": [],
   "source": [
    "from urllib.request import urlretrieve"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "848b9a18",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "import os\n",
    "\n",
    "output_relative_dir = '../../mast30034-project-1-janggani/data/raw/'\n",
    "if not os.path.exists(output_relative_dir):\n",
    "    os.makedirs(output_relative_dir)\n",
    "    \n",
    "for target_dir in (\"yellow\", \"green\"):\n",
    "    if not os.path.exists(output_relative_dir + target_dir):\n",
    "        os.makedirs(output_relative_dir + target_dir)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "683d7f2b",
   "metadata": {},
   "outputs": [],
   "source": [
    "YEAR = 2019\n",
    "MONTHS = range(1,7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "19f0dde0",
   "metadata": {},
   "outputs": [],
   "source": [
    "URL_TEMPLATE_y = \"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_\"\n",
    "URL_TEMPLATE_g = \"https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "51de6bc4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Begin month 01\n",
      "Completed month 01\n",
      "Begin month 02\n",
      "Completed month 02\n",
      "Begin month 03\n",
      "Completed month 03\n",
      "Begin month 04\n",
      "Completed month 04\n",
      "Begin month 05\n",
      "Completed month 05\n",
      "Begin month 06\n",
      "Completed month 06\n"
     ]
    }
   ],
   "source": [
    "yellow_output_dir = output_relative_dir + 'yellow'\n",
    "\n",
    "for month in MONTHS: \n",
    "    month = str(month).zfill(2)\n",
    "    print(f\"Begin month {month}\")\n",
    "    url = f'{URL_TEMPLATE_y}{YEAR}-{month}.parquet'\n",
    "    output_dir_y = f\"{yellow_output_dir}/{YEAR}-{month}.parquet\"\n",
    "    \n",
    "    urlretrieve(url, output_dir_y)\n",
    "    print(f\"Completed month {month}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "dbeaaaa0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Begin month 01\n",
      "Completed month 01\n",
      "Begin month 02\n",
      "Completed month 02\n",
      "Begin month 03\n",
      "Completed month 03\n",
      "Begin month 04\n",
      "Completed month 04\n",
      "Begin month 05\n",
      "Completed month 05\n",
      "Begin month 06\n",
      "Completed month 06\n"
     ]
    }
   ],
   "source": [
    "green_output_dir = output_relative_dir + 'green'\n",
    "\n",
    "for month in MONTHS: \n",
    "    month = str(month).zfill(2)\n",
    "    print(f\"Begin month {month}\")\n",
    "    url = f'{URL_TEMPLATE_g}{YEAR}-{month}.parquet'\n",
    "    output_dir_g = f\"{green_output_dir}/{YEAR}-{month}.parquet\"\n",
    "    \n",
    "    urlretrieve(url, output_dir_g)\n",
    "    print(f\"Completed month {month}\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
