#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matrix import Matrix

m1 = Matrix([[1,2],[3,4]])
print (m1)
#| 1  2 |
#| 3  4 |

m2 = Matrix([[4,3],[2,1]])
m3 = Matrix([[4,3]])
print (m2)
#| 4  3 |
#| 2  1 |

m3 = m1 + m2
print (m3)
#| 5  5 |
#| 5  5 |

m4 = m1 + 3
print (m4)
#| 4  5 |
#| 6  7 |

m5 = 3 + m1
print (m5)
#| 4  5 |
#| 6  7 |

m6 = m3 - m2
print (m6)
#| 1  2 |
#| 3  4 |

m7 = m3 - 3
print (m7)
#| 2  2 |
#| 2  2 |

m8 = 4 - m1
print (m8)
#| 3  2 |
#| 1  0 |

m9 = m1.prod(m2)
print (m9)
#| 8  5 |
#| 20  13 |
print (m3+m2)
for i in m9:
	print (i)
#[8, 5]
#[20, 13]
