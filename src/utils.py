def remove4(df):
    for year in ['Grades1997','Grades1998','Grades1999','Grades2000','Grades2001','Grades2002','Grades2003','Grades2004','Grades2005','Grades2006','Grades2007']:
    df[year]=np.where(df[year]==-4,0,df[year])
    return df