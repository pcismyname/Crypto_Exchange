  /** @type {import('./$types').PageLoad} */
  export async function load({ parent, params }) {
    const { coinId } = params;
    const { a } = await parent();

    // Here we simulate fetching data from an API with hardcoded data
    const dummyData = {
      btc: {
        name: 'Bitcoin',
        price: '$40,000',
        description: 'Bitcoin is a cryptocurrency invented in 2008.',
        // ... other Bitcoin details
      },
      eth: {
        name: 'Ethereum',
        price: '$3,000',
        description: 'Ethereum is a decentralized, open-source blockchain.',
        // ... other Ethereum details
      },
      usdt: {
        name: 'USDT',
        price: '$1',
        description: 'Tether is a controversial cryptocurrency with tokens.',
        // ... other USDT details
      },
      xrp: {
        name: 'XRP',
        price: '$0.50',
        description: 'XRP is the cryptocurrency used by the Ripple payment network.',
        // ... other XRP details
      },
      // ... other coins
    };

    const data = dummyData[coinId] || {
      name: 'Unknown',
      price: 'Unknown',
      description: 'Details for this coin are not available.',
      // ... default details
    };

    return { coin : a,
      coinDetails: data };
  }
