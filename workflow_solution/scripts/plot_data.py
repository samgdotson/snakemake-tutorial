if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import pandas as pd

    raw_data = pd.read_csv(snakemake.input.data, 
                            usecols=['time', 'kw'],
                            parse_dates=True,
                            index_col='time')
    
    processed_data = pd.read_csv(snakemake.input.processed_data, 
                            usecols=['time', 'kw'],
                            parse_dates=True,
                            index_col='time')
    

    plot_options = snakemake.config['plot_options']
    fig, ax = plt.subplots(**plot_options)

    raw_data.plot(ax=ax)
    processed_data.plot(ax=ax)

    plt.savefig(snakemake.output.plot)