{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "1c9d0e0b",
   "metadata": {},
   "source": [
    "Adapted from prerequisite notebook"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "b3165446",
   "metadata": {},
   "outputs": [],
   "source": [
    "from urllib.request import urlretrieve"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "92bc59e2",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "\n",
    "output_relative_dir = '../../mast30034-project-1-janggani/data/raw/'\n",
    "\n",
    "if not os.path.exists(output_relative_dir):\n",
    "    os.makedirs(output_relative_dir)\n",
    "    \n",
    "for target_dir in (\"yellow\", \"green\"):\n",
    "    if not os.path.exists(output_relative_dir + target_dir):\n",
    "        os.makedirs(output_relative_dir + target_dir) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "8b858bd3",
   "metadata": {},
   "outputs": [],
   "source": [
    "YEAR = '2019'\n",
    "MONTHS = range(1,7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "aae87367",
   "metadata": {},
   "outputs": [],
   "source": [
    "URL_TEMPLATE = \"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "2e1b810d",
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
    "for month in MONTHS:\n",
    "    # 0-fill i.e 1 -> 01, 2 -> 02, etc\n",
    "    month = str(month).zfill(2) \n",
    "    print(f\"Begin month {month}\")\n",
    "    \n",
    "    # generate url\n",
    "    url = f'{URL_TEMPLATE}{YEAR}-{month}.parquet'\n",
    "    # generate output location and filename\n",
    "    output_dir = f\"{yellow_output_dir}/{YEAR}-{month}.parquet\"\n",
    "    # download\n",
    "    urlretrieve(url, output_dir) \n",
    "    \n",
    "    print(f\"Completed month {month}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "0285442e",
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
    "for month in MONTHS:\n",
    "    # 0-fill i.e 1 -> 01, 2 -> 02, etc\n",
    "    month = str(month).zfill(2) \n",
    "    print(f\"Begin month {month}\")\n",
    "    \n",
    "    # generate url\n",
    "    url = f'{URL_TEMPLATE}{YEAR}-{month}.parquet'\n",
    "    # generate output location and filename\n",
    "    output_dir = f\"{green_output_dir}/{YEAR}-{month}.parquet\"\n",
    "    # download\n",
    "    urlretrieve(url, output_dir) \n",
    "    \n",
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
