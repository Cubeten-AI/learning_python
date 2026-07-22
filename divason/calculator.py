{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "49ab30b0-8236-4da8-81da-4b167779947c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter ur choice 1/2/3/4: 2\n",
      "enter ur no.1: 3\n",
      "enter ur no.2: 4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sub= -1.0\n"
     ]
    }
   ],
   "source": [
    "choice=int(input(\"enter ur choice 1/2/3/4:\"))\n",
    "n1=float(input(\"enter ur no.1:\"))\n",
    "n2=float(input(\"enter ur no.2:\"))\n",
    "\n",
    "if choice==1:\n",
    "    print(\"sum=\",n1+n2)\n",
    "elif choice==2:\n",
    "    print(\"sub=\",n1-n2)\n",
    "elif choice==3:\n",
    "    print(\"mult=\",n1*n2)\n",
    "elif choice==4:\n",
    "    if n2==0:\n",
    "        print(\"div=\",n1/n2)\n",
    "    else:\n",
    "        print(\"error\")\n",
    "else:\n",
    "    print(\"inavlid choise\")\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e7b58d74-578f-4817-be66-f62a93d2cee7",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
