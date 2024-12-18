const config = {
  schemaFile: './api_schema.yml',
  apiFile: "./emptyApi.ts",
  apiImport: "emptySplitApi",
  outputFile: "./apiStore.gen.ts",
  exportName: "api",
  useEnumType: true,
  hooks: true,
}
module.exports = config