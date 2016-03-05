"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": ("172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0")
            "answer": "172.16.12.0/22"
        }
    ],
    "Extra": [
        {
            "input": ("10.1.57.0", "10.1.59.0", "10.1.61.0")
            "answer": "10.1.56.0/21"
        },
        {
            "input": ("192.168.97.0", "192.168.100.0")
            "answer": "192.168.96.0/21"
        },
        {
            "input": ("172.16.14.0", "172.16.17.0", "172.16.25.0")
            "answer": "172.16.0.0/19"
        },
        {
            "input": ("172.16.14.0", "172.16.17.0", "172.16.25.0", "10.1.57.0", "10.1.59.0", "10.1.61.0")
            "answer": "0.0.0.0/0"
        }

    ]
}
